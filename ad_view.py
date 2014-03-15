<?xml version="1.0" encoding="utf-8"?>
<openerp>
    <data>
	<menuitem id="advert_work_main" name="Activity"/>
	
<record id="view_activity_tree"  model="ir.ui.view">
            <field name="name">advert.activity.tree</field>
            <field name="model">advert.activity</field>
            <field name="arch" type="xml">
                <tree string="Activity">
                    <field name="name"/>
                    <field name="type_of_activity"/>

                </tree>
            </field>
        </record>
		<record id="view_activity_form"  model="ir.ui.view">
            <field name="name">advert.activity.form</field>
            <field name="model">advert.activity</field>
            <field name="arch" type="xml">
            
                <form string="Activity" version="7.0">
 				<sheet>	
 				<group>           
                    <field name="name"/>
                    <field name="type_of_activity"/>

                </group>
                <group>

                  
                </group>
                <grouo>

                </grouo>
                </sheet>
                </form>
            </field>
        </record>
    <menuitem id="activity_score_order" name="Activity" parent="advert_work_main" action="action_activity_course"/>
	 	        
        
        <record model="ir.actions.act_window" id="action_activity_course">
            <field name="name">Activity</field>
            <field name="res_model">advert.activity</field>
            <field name="view_type">form</field>
            <field name="view_mode">form,tree</field>
            <field name="view_id" ref="view_activity_form"/>
        </record>
        
        
<!--         <record id="view_activity_sale_inherit_form"  model="ir.ui.view"> -->
<!--             <field name="name">res.sale.inherit.tree</field> -->
<!--             <field name="model">sale.order</field> -->
<!--             <field name="inherit_id" ref="sale.view_order_form"/> -->
<!--             <field name="arch" type="xml"> -->
<!--                 <data> -->
<!--                     <xpath expr="//field[@name='partner_id']" position="after"> -->
<!--                         <field name="create_activity"/> -->
<!--                         <field name="activity_code"/> -->
<!--                         <field name="purchase_order"/> -->
<!--                     </xpath> -->
<!--                 </data>  -->
<!--             </field> -->
<!--         </record>  -->
        
<!--         <record id="view_purchase_form1"  model="ir.ui.view"> -->
<!--             <field name="name">purchase.order.form.inherit</field> -->
<!--             <field name="model">purchase.order</field> -->
<!--             <field name="inherit_id" ref="purchase.purchase_order_form"/> -->
<!--             <field name="arch" type="xml"> -->
<!--                 <data> -->
<!--                     <xpath expr="//field[@name='origin']" position="after"> -->
<!--                         <field name="create_activity"/> -->
<!--                         <field name="activity_code"/> -->
<!--                         <field name="sale_order"/> -->
<!--                     </xpath> -->
<!--                 </data>  -->
<!--             </field> -->
<!--     </record> -->
        
        
    </data>
</openerp>
