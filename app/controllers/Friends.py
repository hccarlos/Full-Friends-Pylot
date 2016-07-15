"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        query = "SELECT * FROM full_of_friends"
        
        # Run query with inserted data.
        allFriends = self.db.query_db(query)

        return self.load_view('index.html', all_friends=allFriends)

    def add(self):
        #add data from the index.html
        query = "INSERT INTO full_of_friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                'first_name': request.form['fname'],
                'last_name': request.form['lname'],
                'email': request.form['email']
                }
        print 'I can come here'
    #Run query, with dictionary values injected into the query.
        self.db.query_db(query, data)
        print 'I can come here'
        return redirect('/')

    def edit(self, editing_id):
        query = "SELECT * FROM full_of_friends WHERE id = :edit_id"
        # Then define a dictionary with key that matches variable_name in query.
        data = {'edit_id': editing_id}
        # Run query with inserted data.
        editing_friend = self.db.query_db(query, data)
        print editing_friend
        return self.load_view('edit.html', one_friend=editing_friend[0])

    def edit_to_list(self, editing_id):
        query = "UPDATE full_of_friends SET first_name = :first_name, last_name = :last_name, email = :email, created_at = NOW() WHERE id = :id"
        data = {
            'first_name': request.form['first_name'], 
            'last_name':  request.form['last_name'],
            'email': request.form['email'],
            'id': editing_id
            }
        self.db.query_db(query, data)
        return redirect('/')
    def show(self, showing_id):
        query = "SELECT * FROM full_of_friends WHERE id = :show_id"
        # Then define a dictionary with key that matches variable_name in query.
        data = {'show_id': showing_id}
        # Run query with inserted data.
        showing_friend = self.db.query_db(query, data)
        return self.load_view('show.html', one_friend=showing_friend[0])
    def go_back(self):
        return redirect('/')

    def delete(self, deleting_id):
        query = "SELECT * FROM full_of_friends WHERE id = :delete_id"
        # Then define a dictionary with key that matches variable_name in query.
        data = {'delete_id': deleting_id}
        # Run query with inserted data.
        deleting_friend = self.db.query_db(query, data)
        return self.load_view('delete.html', one_friend=deleting_friend[0])

    def delete_from_list(self, deleting_id):
        query = "DELETE FROM full_of_friends WHERE id = :id"
        data = {'id': deleting_id}
        self.db.query_db(query, data)
        return redirect('/')




