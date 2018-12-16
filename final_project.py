from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)



#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]



#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},
{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]


# basically done

@app.route('/')
@app.route('/restaurant/<int:restaurant_id>')
def showRestaurants():

    return render_template('restaurants.html', restaurants = restaurants)


# finished
@app.route("/restaurant/new", methods=['GET', 'POST'])
def newRestaurant():
    # empty dictionary, this is not a database, so even if the function works,
    # it would not hold the data.
    new_restaurants = {}
    if request.method == 'POST':
        new_restaurants['name'] = request.form['name']
        new_restaurants['id'] = request.form['id']
        restaurants.append(new_restaurants)
        # return redirect(url_for('showRestaurants'))
        return redirect(url_for('newMenuItem',restaurant_id = int(request.form['id'])))
    else:
        return render_template('newRestaurant.html')



# finished, notice that the edit query can not go beyond 3, because there are
# only 3 restaurants in the list, therefore, if you make a new restaurant with id 4
# and try to edit it, this won't work, because the new restaurant has never been
# appended to the list. So, it would show an error.
@app.route("/restaurant/<int:restaurant_id>/edit",methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    if request.method == 'POST':
        restaurants[restaurant_id-1]['name']= request.form['name']
        restaurants[restaurant_id-1]['id']=  request.form['id']
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html',restaurants = restaurants,restaurant_id=restaurant_id)

    # return "This page will be for editing restaurant"#  %s" % restaurant_id


# notice that because the inability of list to properly handle update of data
# when delete an restaurant, it may cause inconsistency. like if you delete restaurant
# b,it may actually delete restaurant a. depends on how messed up the list query become.
@app.route("/restaurant/<int:restaurant_id>/delete",methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    if request.method == 'POST':

        # this deletes the whole dictionary from the list.
        del restaurants[restaurant_id]
        return redirect(url_for('showRestaurants'))

    else:
    # return "This page will be for deleting restaurant"# %s" % restaurant_id
        return render_template('deleteRestaurant.html', restaurants = restaurants,restaurant_id=restaurant_id)


# tested menu.html, everything works
@app.route("/restaurant/<int:restaurant_id>/menu")
def showMenu(restaurant_id):
    # matching the id between restaurant and items
    item = {}
    for i in items:
        if (int(i['id'])) == (restaurant_id):
            item = i
    # return "This page is the menu for rstaurant"#  %s" % restaurant_id|
    return render_template('menu.html', restaurants = restaurants, items = item, restaurant_id = restaurant_id)


# this function is called after a new restaurant is created, it does not have to be the
# the only menu item for the new restaurant, but because I wanted the id of the items
# match the id of the restaurant, so it was designed this way. in a database setting,
# this will be different, as a database can handle matching of ids between restaurant and
# items.
@app.route("/restaurant/<int:restaurant_id>/menu/new" ,methods = ['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        item = {}
        item['name'] = request.form['name']
        item['price'] = request.form['price']
        item['course'] = request.form['course']
        item['price'] = request.form['price']
        item['id'] = restaurant_id
        items.append(item)
        return redirect(url_for('showRestaurants'))
    else:
        render_template('newMenuItem.html',restaurants = restaurants,restaurant_id = restaurant_id)

    # add item to dictionary default_data['item3'] = 3

    # return "This page is for making a new menu item for restaurant"# %s" %s restaurant_id|
    return render_template('newMenuItem.html', restaurants = restaurants,restaurant_id =restaurant_id)


# Almost finished, but items edited may not match to its restaurants, because of the restaurant and item lists
# could not be updated
@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit", methods = ['GET','POST'])
def editMenuItem(restaurant_id,menu_id):
    # return "This page is for editing menu item"#  %s" % menu_id|

    if request.method == 'POST':

        return redirect(url_for('showMenu',restaurant_id=restaurant_id))
    else:
        return render_template('editMenuItem.html', restaurants = restaurants, items = items[menu_id], restaurant_id = restaurant_id,menu_id = menu_id)


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete", methods = ['GET','POST'])
def deleteMenuItem(restaurant_id,menu_id):
    # return "This page is for deleting menu item" #  %s" % menu_id |
    if request.method == 'POST':
        del items[menu_id]
        return redirect(url_for('showMenu',restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', restaurants = restaurants, items= items[menu_id], restaurant_id = restaurant_id,menu_id = menu_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
