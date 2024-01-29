#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| item_rarity.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:22:51
# Last Modified: Mo, January 29th 2024, 22:27:28

from .wiki_base import Base

class ItemRarity(Base):

    class Meta:
            verbose_name        = "Item Rarity"
            verbose_name_plural = "Item Rarities"