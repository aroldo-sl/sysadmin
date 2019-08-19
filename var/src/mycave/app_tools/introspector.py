#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# @file:    
# @date:    2012-05-22
# @author:  Thomas Kaspari
# @mail:    kaspari@mitcon.de
# @mail:    tomka@lypke.de

'''
tiny introspection tool for grok
'''    
import types
import grok
from ..app import Mycave

grok.templatedir('tools_templates')

class MyIntrospector (grok.View):
    ''' simple introspector for ZODB '''
    grok.context(Mycave)
    grok.name('introspector')
    grok.template('introspector')
    
    _traversal_path = []
    
    def traversal_path(self):
        return self._traversal_path
    
    def path_data(self):
        data = {}
        folder = self.context
        for folder_id in self._traversal_path:
            try:
                folder = folder[folder_id]
            except:
                folder = folder #TODO: not the correct solution
                    
        try:
            for obj in folder:
                data[obj] = folder[obj]
        except:
            pass
            
        return data
        
    def data(self):
        attributes_dict = {}
        type_dict       = {}
        method_list     = []
        attribute_list  = []
        obj = self.context
        for obj_id in self._traversal_path:
            try:
                obj = obj[obj_id]
            except:
                pass
        
        fields = dir(obj)
        for field in fields:
            if not field[0] == '_':
                try:
                    attributes_dict[field] = getattr(obj, field)
                except:
                    attributes_dict[field] = u"error"
                
                data_type = type(attributes_dict[field])
                type_dict[field] = data_type
                
                if data_type == types.MethodType:
                    method_list.append(field)
                else:
                    attribute_list.append(field)  
        
        #sorted_keys = attributes_dict.keys()
        #sorted_keys.sort()
        method_list.sort()
        attribute_list.sort()
        data = {}
        data['attributes_dict'] = attributes_dict
        data['type_dict']       = type_dict
        data['method_list']     = method_list
        data['attribute_list']  = attribute_list
        #data['sorted_keys']=sorted_keys
        return data
    
    def update(self):
        '''  '''
        submit = self.request.form.get('choose', None)
        if submit:
            self._traversal_path.append(submit)
            
            
            
        submit = self.request.form.get('return', None)
        if submit:
            try:
                self._traversal_path.pop(-1)
            except:
                self._traversal_path = []
        
    




