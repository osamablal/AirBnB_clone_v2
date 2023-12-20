#!/usr/bin/python3
"""The class of File-Storage."""
import json
import models


classes = {"State": models.state.State, "City": models.city.City,
           "User": models.user.User, "Place": models.place.Place,
           "Review": models.review.Review, "Amenity": models.amenity.Amenity}

class FileStorage:
    """
        Putting instances to JSON and deputting to JSON.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
            Going back to the dictinary.
        """
        fsss_objects = {}
        if cls:
            if isinstance(cls) is str and cls in classes:
                for key, val in self.__objects.items():
                    if cls == key.split('.')[0]:
                        fsss_objects[key] = val
            elif cls.__name__ in classes:
                for key, val in self.__objects.items():
                    if cls.__name__ == key.split('.')[0]:
                        fsss_objects[key] = val
        else:
            return self.__objects
        return fsss_objects

    def new(self, obj):
        """
            Putting the object with key <obj class name> id.
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
            Putting objects attriebute to JSON.
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
            Deputting the JSON file to objects.
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deleting object from objects.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]
        self.save()

    def close(self):
        """
        Calling for reload.
        """
        self.reload()

