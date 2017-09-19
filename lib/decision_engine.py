import yaml
import os
from db import MysqlDB


class DecisionEngine():

    def __init__(self, app, config):
        self.db = MysqlDB()
        self.db.get_connection(app, config)

    def update_rule(self, slot_id, article, cross_products, ad, insert):
        if insert:

            query = "insert into dc_rules(slot_id, article, cross_product, ad) values({0},{1},{2},{3})"\
                .format(slot_id, article, cross_products, ad)
            print query
        else:
            query = "update dc_rules SET article={0}, cross_product={1}, ad={2} where slot_id={3};"\
                .format(article,
                        cross_products,
                        ad,
                        slot_id)
        return self.db.update_query(query=query)

    def get_rules(self):
        query = "select * from dc_rules"
        rules = self.db.query(query=query)
        if len(rules)!=0:
            rules_data = []
            for row in rules:
                rules_data.append({
                    'slot_id': row[0],
                    'article': row[1],
                    'cross_product': row[2],
                    'ad': row[3]
                })
            return rules_data
        else:
            return {'message': 'no data available'}


    def get_slot_info(self, slot_id):
        query = "select * from dc_rules where slot_id={slot_id}".format(slot_id=slot_id)
        return self.db.query(query=query)
