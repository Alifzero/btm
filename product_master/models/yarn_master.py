from odoo import models, fields, api, _
from odoo.exceptions import UserError


#
# class YarnMasterProductCreation(models.Model):
#     _name = 'yarn.master.product'
#
#     name = fields.Char(string='Yarn Name', )
#     code = fields.Char(string='Yarn Code', compute='YarnCode')
#     business_line = fields.Many2one('business.line')
#     item_group = fields.Many2one('product.category')
#     item_category = fields.Many2one('product.category')
#     yarn_category = fields.Many2one('product.category')
#     greige_dyed = fields.Many2one('greige.dyed')
#     yarn_count = fields.Many2one('yarn.count')
#     yarn_structure = fields.Many2one('yarn.structure')
#     yarn_composition = fields.Many2one('yarn.composition')
#     yarn_level = fields.Many2one('yarn.level')
#     yarn_waving_loom = fields.Many2one('yarn.waving.loom')
#
#     def YarnCode(self):
#         yarn_code = str(self.yarn_category.name)
#         self.code = yarn_code
#
#     # @api.onchange('item_group', 'greige_dyed', 'yarn_count', 'yarn_structure', 'yarn_composition', 'yarn_category')
#     def createYarnName(self):
#         try:
#             item_group = self.item_group.name
#             item_category = self.item_category.name
#             greige_dyed = self.greige_dyed.name
#             yarn_count = self.yarn_count.name
#             yarn_structure = self.yarn_structure.name
#             yarn_composition = self.yarn_composition.name
#             yarn_category = self.yarn_category.name
#
#             name = str(item_group) + ' ' + str(greige_dyed) + '- ' + str(yarn_composition) + ' ' + str(
#                 yarn_structure) + '-' + str(
#                 yarn_count) + ' ' + str(yarn_category)
#             self.name = name
#
#             self.env['product.template'].create({
#                 'name': name,
#                 # 'sub_categ_id': item_category,
#                 # 'yarn_sub_categ_id': yarn_category,
#             })
#         except:
#             raise UserError(_('Error while creating Yarn Product Name'))


class inheritProductCategory(models.Model):
    _inherit = 'product.category'

    code = fields.Char(string='Code')


class BusinessLine(models.Model):
    _name = 'business.line'

    name = fields.Char(string='Business Line', required=True)


# Key Information


class GreigeDyedKeyInformation(models.Model):
    _name = 'greige.dyed'

    name = fields.Char(string='Greige/Dyed', required=True)


class YarnCountKeyInformation(models.Model):
    _name = 'yarn.count'

    name = fields.Char(string='Yarn Count', required=True)


class YarnstructureKeyInformation(models.Model):
    _name = 'yarn.structure'

    name = fields.Char(string='Yarn Structure', required=True)


class YarnCompositionKeyInformation(models.Model):
    _name = 'yarn.composition'

    name = fields.Integer(string='Yarn Composition', required=True)


class YarnLevelKeyInformation(models.Model):
    _name = 'yarn.level'

    name = fields.Char(string='Yarn Level', required=True)


class YarnWeavingLoomKeyInformation(models.Model):
    _name = 'yarn.weaving.loom'

    name = fields.Char(string='Yarn Waving Loom', required=True)


class yarnProductCategoryProductTemplate(models.Model):
    _inherit = 'product.template'

    master_product = fields.Selection([
        ('yarn_master', 'Yarn Master'),
        ('item_master', 'Item Master'),
    ],
        required=True)

    item_name = fields.Char(string='Item Name', )
    name = fields.Char(required=False, related='name_temp')
    name_temp = fields.Char(compute='createYarnName')

    sub_categ_id = fields.Many2one('product.category', 'Item Category', )
    yarn_sub_categ_id = fields.Many2one('product.category', 'Yarn Category',)

    code = fields.Char(string='Yarn Code', compute='YarnCode')
    code_temp = fields.Char()
    business_line = fields.Many2one('business.line')
    item_group = fields.Many2one('product.category')
    item_category = fields.Many2one('product.category')
    yarn_category = fields.Many2one('product.category')
    greige_dyed = fields.Many2one('greige.dyed')
    yarn_count = fields.Many2one('yarn.count')
    yarn_structure = fields.Many2one('yarn.structure')
    yarn_composition = fields.Many2one('yarn.composition')
    yarn_level = fields.Many2one('yarn.level')
    yarn_weaving_loom = fields.Many2one('yarn.weaving.loom')

    @api.model
    def create(self, vals):
        record = super(yarnProductCategoryProductTemplate, self).create(vals)
        record['code_temp'] = self.env['ir.sequence'].next_by_code('product_code_seq') or ('New')
        return record

    def YarnCode(self):
        yarn_code = str(self.item_category.code) + '-' + str(self.item_group.code) + '-' + str(self.code_temp)
        self.code = yarn_code

    # @api.onchange('name_temp')
    # def ProductName(self):
    #     self.name = self.name_temp

    # @api.onchange('master_product', 'item_group', 'greige_dyed', 'yarn_composition', 'yarn_structure', 'yarn_count',
    #               'yarn_category')
    def createYarnName(self):
        try:
            if self.master_product == 'yarn_master':
                item_group = self.item_group.name
                item_category = self.item_category.name
                greige_dyed = self.greige_dyed.name
                yarn_count = self.yarn_count.name
                yarn_structure = self.yarn_structure.name
                yarn_composition = self.yarn_composition.name
                yarn_category = self.yarn_category.name

                name = str(item_group) + ' ' + str(greige_dyed) + '- ' + str(yarn_composition) + ' ' + str(
                    yarn_structure) + '-' + str(
                    yarn_count) + ' ' + str(yarn_category)
                self.name_temp = name

            else:
                self.name_temp = self.item_name
        except:
            pass

    # @api.onchange('yarn_name','master_product')
    # def productNameYarn(self):
    #
    #     if self.master_product == 'yarn_master':
    #         self.name = self.yarn_name
    #     else:
    #         pass

    item_description = fields.Char()
    item_code = fields.Char()
    manual_code = fields.Char()
    primary_uom = fields.Many2one('uom.uom')
    secondary_uom = fields.Many2one('uom.uom')

    remarks = fields.Text()
