#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background


class EntityFactory:
    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'Leve1Bg':
                list_bg = []
                for i in range (7):
                    list_bg.append(Background(name=f'Level1Bg{i}'))
                return list_bg
