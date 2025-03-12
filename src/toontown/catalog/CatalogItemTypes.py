import CatalogFurnitureItem
import CatalogChatItem
import CatalogClothingItem
import CatalogEmoteItem
import CatalogWallpaperItem
import CatalogFlooringItem
import CatalogWainscotingItem
import CatalogMouldingItem
import CatalogWindowItem
import CatalogPoleItem
import CatalogPetTrickItem
import CatalogBeanItem
import CatalogGardenItem
import CatalogInvalidItem
import CatalogRentalItem
import CatalogGardenStarterItem
import CatalogToonStatueItem
import CatalogAnimatedFurnitureItem
import CatalogAccessoryItem
import CatalogHouseItem
INVALID_ITEM = 0
FURNITURE_ITEM = 1
CHAT_ITEM = 2
CLOTHING_ITEM = 3
EMOTE_ITEM = 4
WALLPAPER_ITEM = 5
WINDOW_ITEM = 6
FLOORING_ITEM = 7
MOULDING_ITEM = 8
WAINSCOTING_ITEM = 9
POLE_ITEM = 10
PET_TRICK_ITEM = 11
BEAN_ITEM = 12
GARDEN_ITEM = 13
RENTAL_ITEM = 14
GARDENSTARTER_ITEM = 15
TOON_STATUE_ITEM = 16
ANIMATED_FURNITURE_ITEM = 17
ACCESSORY_ITEM = 18
HOUSE_ITEM = 19
NonPermanentItemTypes = (RENTAL_ITEM,)
CatalogItemTypes = {CatalogInvalidItem.CatalogInvalidItem: INVALID_ITEM,
 CatalogFurnitureItem.CatalogFurnitureItem: FURNITURE_ITEM,
 CatalogChatItem.CatalogChatItem: CHAT_ITEM,
 CatalogClothingItem.CatalogClothingItem: CLOTHING_ITEM,
 CatalogEmoteItem.CatalogEmoteItem: EMOTE_ITEM,
 CatalogWallpaperItem.CatalogWallpaperItem: WALLPAPER_ITEM,
 CatalogWindowItem.CatalogWindowItem: WINDOW_ITEM,
 CatalogFlooringItem.CatalogFlooringItem: FLOORING_ITEM,
 CatalogMouldingItem.CatalogMouldingItem: MOULDING_ITEM,
 CatalogWainscotingItem.CatalogWainscotingItem: WAINSCOTING_ITEM,
 CatalogPoleItem.CatalogPoleItem: POLE_ITEM,
 CatalogPetTrickItem.CatalogPetTrickItem: PET_TRICK_ITEM,
 CatalogBeanItem.CatalogBeanItem: BEAN_ITEM,
 CatalogGardenItem.CatalogGardenItem: GARDEN_ITEM,
 CatalogRentalItem.CatalogRentalItem: RENTAL_ITEM,
 CatalogGardenStarterItem.CatalogGardenStarterItem: GARDENSTARTER_ITEM,
 CatalogToonStatueItem.CatalogToonStatueItem: TOON_STATUE_ITEM,
 CatalogAnimatedFurnitureItem.CatalogAnimatedFurnitureItem: ANIMATED_FURNITURE_ITEM,
 CatalogAccessoryItem.CatalogAccessoryItem: ACCESSORY_ITEM,
 CatalogHouseItem.CatalogHouseItem: HOUSE_ITEM}
CatalogItemTypeMask = 31
CatalogItemSaleFlag = 128
CatalogItemGiftTag = 64
