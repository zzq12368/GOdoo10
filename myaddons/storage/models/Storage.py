# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class StorageXiaoliao(models.Model):
    """ Model for case stages. This models the main stages of a Maintenance Request management flow. """

    _name = 'storage.xiaoliao'
    _description = 'Storage xiaoliao'
    _order = 'id'

    inDate = fields.Datetime()
    name = fields.Char('材料名称', required=True)

class StorageXiaoliaoCategory(models.Model):
    _name = "storage.xiaoliao.category"
    _description = "Product Category"
    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'name'

    name = fields.Char('Name', index=True, required=True, translate=True)
    parent_id = fields.Many2one('storage.xiaoliao.category', 'storage Category', index=True, ondelete='cascade')
    child_id = fields.One2many('storage.xiaoliao.category', 'parent_id', 'Child Categories')
    parent_left = fields.Integer('Left Parent', index=1)
    parent_right = fields.Integer('Right Parent', index=1)

    @api.multi
    def name_get(self):
        def get_names(cat):
            """ Return the list [cat.name, cat.parent_id.name, ...] """
            res = []
            while cat:
                res.append(cat.name)
                cat = cat.parent_id
            return res

        return [(cat.id, " / ".join(reversed(get_names(cat)))) for cat in self]

class StorageVendor(models.Model):
    _name = "storage.vendor"
    _description = "storage vendor"
    name = fields.Char('Name', index=True, required=True, translate=True)
    type = fields.Selection([
        ('XL', '小料供货商'),
        ('DL', '大料供货商'),
        ('ALL','小料、大料供货商')], 'Type', default='XL' )



