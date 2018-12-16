from flask import Flask, render_template

app = Flask(__name__)



#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]



#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}



@app.route('/')
@app.route('/restaurant/<int:restaurant_id>')
def showRestaurants(restaurant_id):

    return render_template('restaurants.html', restaurants = restaurants, restaurant_id = restaurant_id)

@app.route("/restaurant/new" )
def newRestaurant():
    #
    return render_template('newRestaurant.html', restaurants = restaurants)

@app.route("/restaurant/restaurant_id/edit")
def editRestaurant():
    # return "This page will be for editing restaurant"#  %s" % restaurant_id
    return render_template('editRestaurant.html', restaurants = restaurants)

@app.route("/restaurant/restaurant_id/delete")
def deleteRestaurant():
    # return "This page will be for deleting restaurant"# %s" % restaurant_id
    return render_template('editRestaurant.html', restaurants = restaurants)



@app.route("/restaurant/<int:restaurant_id>/menu")
def showMenu(restaurant_id):
    item = {}
    for i in items:
        if (int(i['id'])) == (restaurant_id):
            item = i
    # return "This page is the menu for rstaurant"#  %s" % restaurant_id|
    return render_template('menu.html', restaurants = restaurants, items = item, restaurant_id = restaurant_id)

@app.route("/restaurant/restaurant_id/menu/new")

def newMenuItem():
    # return "This page is for making a new menu item for restaurant"# %s" %s restaurant_id|
    return render_template('newMenuItem.html', restaurants = restaurants)

@app.route("/restaurant/restaurant_id/menu/menu_id")
def editMenuItem():
    # return "This page is for editing menu item"#  %s" % menu_id|
    return render_template('editMenuItem.html', restaurants = restaurants, items = items)


@app.route("/restaurant/restaurant_id/menu/menu_id/delete")
def deleteMenuItem():
    # return "This page is for deleting menu item" #  %s" % menu_id |
    return render_template('deleteMenuItem.html', restaurants = restaurants, items= items )

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
