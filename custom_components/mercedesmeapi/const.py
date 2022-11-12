"""
Mercedes Me APIs

Author: G. Ravera

For more details about this component, please refer to the documentation at
https://github.com/xraver/mercedes_me_api/
"""
# Software Name & Version
NAME = "Mercedes Me API"
DOMAIN = "mercedesmeapi"
VERSION = "0.11"
# Software Parameters
TOKEN_FILE = ".mercedesme_token"
RESOURCES_FILE = ".mercedesme_resources"
# Mercedes me Application Parameters
REDIRECT_URL = "https://localhost"
SCOPE = "openid%20mb:vehicle:mbdata:fuelstatus%20mb:vehicle:mbdata:vehiclestatus%20mb:vehicle:mbdata:vehiclelock%20mb:vehicle:mbdata:evstatus%20mb:vehicle:mbdata:payasyoudrive%20offline_access"
URL_RES_PREFIX = "https://api.mercedes-benz.com/vehicledata/v2"
#UPDATE_SIGNAL = "mercedesmeapi_update"

# Configuration File Parameters
CONF_CLIENT_ID = "client_id"
CONF_CLIENT_SECRET = "client_secret"
CONF_VEHICLE_ID = "vehicle_id"
CONF_ENABLE_RESOURCES_FILE = "enable_resources_file"
