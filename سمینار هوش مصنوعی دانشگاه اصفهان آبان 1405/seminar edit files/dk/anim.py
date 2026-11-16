# -*- coding: utf-8 -*-
"""Slide transitions and entrance animations (native PowerPoint timing XML)."""
from lxml import etree
from pptx.oxml.ns import qn

P = "http://schemas.openxmlformats.org/presentationml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"


def _el(tag, **attrs):
    e = etree.SubElement(etree.Element("dummy"), qn(tag))
    for k, v in attrs.items():
        e.set(k, str(v))
    return e


def _sub(parent, tag, **attrs):
    e = etree.SubElement(parent, qn(tag))
    for k, v in attrs.items():
        e.set(k, str(v))
    return e


def transition(slide, kind="fade", speed="med"):
    sld = slide._element
    old = sld.find(qn("p:transition"))
    if old is not None:
        sld.remove(old)
    tr = etree.Element(qn("p:transition"))
    tr.set("spd", speed)
    etree.SubElement(tr, qn("p:" + kind))
    # schema order: cSld, clrMapOvr, transition, timing, extLst
    clr = sld.find(qn("p:clrMapOvr"))
    if clr is not None:
        clr.addnext(tr)
    else:
        sld.find(qn("p:cSld")).addnext(tr)


def animate(slide, shapes, dur=0.45, gap=0.10, delay=0.15):
    """Fade-in a list of shapes sequentially, auto-starting with the slide."""
    ids = [s.shape_id for s in shapes if s is not None]
    if not ids:
        return
    sld = slide._element
    old = sld.find(qn("p:timing"))
    if old is not None:
        sld.remove(old)

    timing = etree.Element(qn("p:timing"))
    tnLst = _sub(timing, "p:tnLst")
    par0 = _sub(tnLst, "p:par")
    ctn1 = _sub(par0, "p:cTn", id=1, dur="indefinite", restart="never", nodeType="tmRoot")
    ch1 = _sub(ctn1, "p:childTnLst")
    seq = _sub(ch1, "p:seq", concurrent="1", nextAc="seek")
    ctn2 = _sub(seq, "p:cTn", id=2, dur="indefinite", nodeType="mainSeq")
    ch2 = _sub(ctn2, "p:childTnLst")
    par3 = _sub(ch2, "p:par")
    ctn3 = _sub(par3, "p:cTn", id=3, fill="hold", nodeType="afterEffect")
    st3 = _sub(ctn3, "p:stCondLst")
    _sub(st3, "p:cond", delay="0")
    ch3 = _sub(ctn3, "p:childTnLst")
    par4 = _sub(ch3, "p:par")
    ctn4 = _sub(par4, "p:cTn", id=4, fill="hold")
    st4 = _sub(ctn4, "p:stCondLst")
    _sub(st4, "p:cond", delay=str(int(delay * 1000)))
    ch4 = _sub(ctn4, "p:childTnLst")

    nid = 10
    for k, sid in enumerate(ids):
        par = _sub(ch4, "p:par")
        ctn = _sub(par, "p:cTn", id=nid, presetID=10, presetClass="entr", presetSubtype=0,
                   fill="hold", grpId=0, nodeType="afterEffect" if k else "withEffect")
        st = _sub(ctn, "p:stCondLst")
        _sub(st, "p:cond", delay="0")
        ch = _sub(ctn, "p:childTnLst")
        # visibility set
        st_el = _sub(ch, "p:set")
        bh = _sub(st_el, "p:cBhvr")
        _sub(bh, "p:cTn", id=nid + 1, dur=1, fill="hold").append(_cond(0))
        tg = _sub(bh, "p:tgtEl")
        _sub(tg, "p:spTgt", spid=sid)
        an = _sub(bh, "p:attrNameLst")
        _sub(an, "p:attrName").text = "style.visibility"
        to = _sub(st_el, "p:to")
        _sub(to, "p:strVal", val="visible")
        # fade
        ae = _sub(ch, "p:animEffect", transition="in", filter="fade")
        bh2 = _sub(ae, "p:cBhvr")
        _sub(bh2, "p:cTn", id=nid + 2, dur=str(int(dur * 1000)))
        tg2 = _sub(bh2, "p:tgtEl")
        _sub(tg2, "p:spTgt", spid=sid)
        nid += 3

    prev = _sub(seq, "p:prevCondLst")
    c = _sub(prev, "p:cond", evt="onPrev", delay=0)
    _sub(_sub(c, "p:tgtEl"), "p:sldTgt")
    nxt = _sub(seq, "p:nextCondLst")
    c2 = _sub(nxt, "p:cond", evt="onNext", delay=0)
    _sub(_sub(c2, "p:tgtEl"), "p:sldTgt")

    tr = sld.find(qn("p:transition"))
    if tr is not None:
        tr.addnext(timing)
    else:
        sld.find(qn("p:cSld")).addnext(timing)


def _cond(delay):
    e = etree.Element(qn("p:stCondLst"))
    c = etree.SubElement(e, qn("p:cond"))
    c.set("delay", str(delay))
    return e
