from toontown.base import TTLocalizer

USER_CANCEL = 0
CHANGE = 1

INVALID_ITEM = 0
SAME_ITEM = 1
NOT_ENOUGH_MONEY = 2
CHANGE_SUCCESSFUL = 3

ChangeMessagesColor = {
 INVALID_ITEM: TTLocalizer.GloveInvalidColorMessage,
 SAME_ITEM: TTLocalizer.NametagColorGuiSameColor,
 NOT_ENOUGH_MONEY: TTLocalizer.GloveNoMoneyMessage,
 CHANGE_SUCCESSFUL: TTLocalizer.NametagColorPurchaseSuccess
}

ChangeMessagesStyle = {
 INVALID_ITEM: TTLocalizer.NametagInvalidStyleMessage,
 SAME_ITEM: TTLocalizer.NametagStyleGuiSameStyle,
 NOT_ENOUGH_MONEY: TTLocalizer.NametagStyleMoreMoneyMessage,
 CHANGE_SUCCESSFUL: TTLocalizer.NametagStylePurchaseSuccess
}
