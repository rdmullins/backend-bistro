# Backend Bistro
## Roger Mullins

**Backend Bistro** is a PostgreSQL-powered Django backend data source used to populate menu items for Gitgrub, a fusion restaurant in Lexington, KY.

The main API is a plug-and-play replacement for an earlier hosted API that suddenly went offline. It delivers information about the various dishes with lookups for category and cuisine style.

## Endpoints

|Address|Description
|----------|--------|
/menu/fullmenu | Main API; returns JSON response with dish title, price, description, and nested cuisine and menu category information|
/menu/eggdishes| Returns a user-friendly list of all dishes in the database they use eggs or egg products. Handy reference for customers or servers in the event of allergies
/menu/dairy| Similar to eggdishes, but lists (in a user-friendly format) dishes that have dairy products in their ingredients
/menu/appetizers|Similar to fullmenu, but filtered to return only appetizers (returns JSON)
/menu/breakfast|Similar to fullmenu, but filtered to return only breakfast items (returns JSON)
/menu/brunch|Similar to fullmenu, but filtered to return only brunch selections (returns JSON)
/menu/lunch|Similar to fullmenu, but filtered to return only lunch (returns JSON)
/menu/dinner|Similar to fullmenu, but filtered to return only dinner  entrees (returns JSON)
/menu/sides|Similar to fullmenu, but filtered to return only side dish items (returns JSON)
/menu/desserts|Similar to fullmenu, but filtered to return only desserts (returns JSON)