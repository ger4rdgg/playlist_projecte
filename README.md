# Playlist Project

This is a project for the web project subject, where we are working with django to implement a web 2.0 page. The idea of ​​our page consists of an automatic playlist generator for spotify through the introduction of desired tags by the user. This is the 2nd order of the project.

## Prerequisites

If you are interested in knowing how to work with the application and reviewing code we worked with you should:

- Have Pycharm installed

- Have python 3.7

- Have pip installed

## Installing

First of all you should create a virtual environment inside the project after cloning it from Github:
```
$pip install virtualenv
```
Here you create the environment:
```
$virtualenv venv
```
And here you activate it:
```
$source /bin/venv/activate
 ```
In order to enable the “behave” command, install the following:
```
behave~=1.2.6
splinter~=0.13.0
$wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
```

## Running the app

Once you are inside the project you can try to run the server by entering this command: 
```
$python manage.py runserver
```
So you can have a look at what the application looks like in the moment.
 
## News

In this 2nd assignment we implemented Features and we have created a way to work with Spotify API so we can use its methods to develop our application.
We have implemented the following methods:

- create_playlist

- modify_playlist

- delete_playlist

## URL Paths

Create Playlist:
```
path('playlists/create/', views.playlist_create, name='playlist_create')
```
View Playlists:
```
path('playlists/list', views.playlist_list, name='playlist_list')
```
View a Playlist’s Details:
```
path('playlists/<int:pk>/', views.list_detail, name='list_detail')
```
Edit Playlist:
```
path('playlists/edit/<int:pk>', views.playlist_update, name='list_update')
```
Delete Playlist:
```
path('playlists/delete/<int:pk>/', views.playlist_remove, name='list_remove')
```


## Built With

- Pycharm
 
- Version Control in Github: https://github.com/ger4rdgg/playlist_projecte
 
## Authors

Gerard Gonzalez, Robert Munné, Arnau Molins, Pau Francino and Mario Martí

See also the list of contributors who participated in this project.
