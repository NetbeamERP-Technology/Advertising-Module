import time
import pytz
from openerp import SUPERUSER_ID
from datetime import datetime
from dateutil.relativedelta import relativedelta

from openerp.osv import fields, osv
from openerp import netsvc
from openerp import pooler
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from openerp.osv.orm import browse_record, browse_null
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP

class advert_activity(osv.osv):
    _name = 'advert.activity'
    _description = 'Advertising Activity'
    _columns = {
                'name':fields.char('Activity Code', readonly=True),
                'type_of_activity': fields.selection([('hording', 'Hoarding'),
                                  ('roadshow', 'Road Show'),
                                  ('creative', 'Creative'),
                                  ('papermedia', 'Paper Media')], 'Type Of Activity', required=True),
                'client_name':fields.many2one('res.partner', 'Client Name', required=True),
                'description':fields.text('Activity Description'),
                'date_s':fields.datetime('Start Date'),
                'date_e':fields.datetime('End Date'),
                'Duration':fields.char('Duration'),
                
                
                }
    
    def create(self, cr, uid, vals, context=None):
        sequence=self.pool.get('ir.sequence').get(cr, uid, 'advert.activity.seq')
        vals['name']=sequence
        return super(advert_activity, self).create(cr, uid, vals, context=context)
    




 #   def create(self, cr, uid, vals, context=None):
 ##       if vals.get('create_activity'):
  #          course_obj=self.pool.get('advert.activity')
  #          sequence=self.pool.get('ir.sequence').get(cr, uid, 'advert.activity.seq')
  #     #     new_course=course_obj.create(cr, uid, {'name':sequence,'purchase_order':vals.get('purchase_order')}, context=context)
  #          vals['activity_code']=sequence            
  #      return super(advert_activity_purchase, self).create(cr, uid, vals, context=context)
