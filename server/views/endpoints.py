#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    endpoints.py
    ~~~~~~~~~~~~

    :copyright: (c) 2015 by Mek.
    :license: see LICENSE for more details.
"""

from flask import render_template, jsonify
from flask.views import MethodView
from api.scholar import FindIt


class PubmedJournal(MethodView):
    def get(self, pmid):
        kwargs = {'oid': pmid} if pmid.startswith('10.1002') else {'pmid': pmid}
        source = FindIt(**kwargs)
        return jsonify({
            'meta': source.to_dict(),
            'article': source.pma.to_dict(),
            'pmid': source.pmid
        })


class Pubmed(MethodView):
    def get(self):
        return 'Paginated list of available journals coming soon.'


class Journals(MethodView):
    def get(self):
        return jsonify({'journals': ['pubmed']})


urls = (
    '/pubmed/<pmid>', PubmedJournal,
    '/pubmed', Pubmed,
    '/', Journals
)
