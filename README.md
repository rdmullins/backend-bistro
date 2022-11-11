# Backend Bistro
## Roger Mullins

**Backend Bistro** is a PostgreSQL-powered Django backend data source used to populate menu items for Gitgrub, a fusion restaurant in Lexington, KY.

The main API is a plug-and-play replacement for an earlier hosted API that suddenly went offline. It delivers information about the various dishes with lookups for category and cuisine style.

## Endpoints

|Address|Description
|----------|--------|
/menu/fullmenu | Main API; returns JSON response with dish title, price, description, and nested cuisine and menu category information|
/menu/appetizers|Similar to fullmenu, but filtered to return only appetizers
/menu/breakfast|Similar to fullmenu, but filtered to return only breakfast items
/menu/brunch|Similar to fullmenu, but filtered to return only brunch selections
/menu/lunch|Similar to fullmenu, but filtered to return only lunch
/menu/dinner|Similar to fullmenu, but filtered to return only dinner entrees
/menu/sides|Similar to fullmenu, but filtered to return only side dish items
/menu/desserts|Similar to fullmenu, but filtered to return only desserts






