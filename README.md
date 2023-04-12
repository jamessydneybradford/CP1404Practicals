# CP1404 Practicals repository

## Details

Author: James Bradford

This repository is a practice repository and is meant be used for
testing purposes only

The concept of clean code is very important.
Code should be readable to all developers so that they can understand it.

Some points that are worthy of consideration are as follows:

- Use the same vocabulary for the same type of variable

        If the entity is the same, you should be consistent in referring to it 
        in your functions. In the following example it is clear that we are refering 
        to user FOR EACH FUNCTION.
    
        def get_user_info(): pass
        def get_user_data(): pass
        def get_user_record(): pass
        
        def get_data() is not clear.

- Use searchable names

  We will read more code than we will ever write.
  It's important that the code we do write is readable and searchable.
  For example:

        import time

        Declare them in the global namespace for the module.
        SECONDS_IN_A_DAY = 60 * 60 * 24
        time.sleep(SECONDS_IN_A_DAY)

        time.sleep(86400) is not bad

- Use explanatory variables (preferably from the problem domain).
  If the code refers to cities, then use the word city. For example:

        import re

        address = "One Infinite Loop, Cupertino 95014"
        city_zip_code_regex = r"^[^,\\]+[,\\\s]+(?P<city>.+?)\s*(?P<zip_code>\d{5})?$"

- Name your functions clearly

  When naming a function put the words 'this function will' in front of
  the name and see if it makes sense:

  This function will orders - makes no sense

  This function will read_orders_from_file - makes sense


- Don't repeat yourself (DRY)

  Do your absolute best to avoid duplicate code.
  Duplicate code is bad because it means that there's more than one place
  to alter something if you need to change some logic.


- Single Responsibility principle

  A class or module should have one, and only one, reason to change.
  If the class has more than one reason to change then there is a large
  chance that it is too complex to be covered in one class.
  For example if a class is designed to read data from file and generate a report,
  there is a possibility that it may have to be changed in two places -
  the read file part and generate part.
  It is better to have two classes - one for reading data and one for generating the report.

There is much more to learn about coding than meets the eye.
Excellent information can be found using the following links:

The programming patterns:

https://github.com/CP1404/Starter/wiki/Programming-Patterns

CP1404 Practicals instructions repo:

https://github.com/CP1404/Practicals

PEP 8 – Style Guide for Python Code:

https://peps.python.org/pep-0008/

PEP 20 – The Zen of Python:

https://peps.python.org/pep-0020/




