"""Message type identifiers for Action Menus."""

from ...didcomm_prefix import DIDCommPrefix

# To be edited
TEST_SECURITY = "action-menu/1.0/menu"

PROTOCOL_PACKAGE = "aries_cloudagent.protocols.security.v1_0"

MESSAGE_TYPES = DIDCommPrefix.qualify_all(
    {
        # To be edited
        TEST_SECURITY: f"{PROTOCOL_PACKAGE}.messages.menu.Menu"
    }
)

CONTROLLERS = DIDCommPrefix.qualify_all(
    {"action-menu/1.0": f"{PROTOCOL_PACKAGE}.controller.Controller"}
)