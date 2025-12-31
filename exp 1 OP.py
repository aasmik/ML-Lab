Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: D:/ML Aasmi/candidate eliminate.py ================
After example 1
S = ['BTech', 'Senior', 'Good', 'City']
G = [['?', '?', '?', '?']]
----------------------------------------
After example 2
S = ['BTech', '?', 'Good', 'City']
G = [['?', '?', '?', '?']]
----------------------------------------
After example 3
S = ['BTech', '?', 'Good', 'City']
G = [['BTech', '?', '?', '?'], ['?', '?', 'Good', '?'], ['?', '?', '?', 'City']]
----------------------------------------
After example 4
S = ['BTech', '?', 'Good', '?']
G = [['BTech', '?', '?', '?'], ['?', '?', 'Good', '?']]
----------------------------------------

Final Specific Boundary: ['BTech', '?', 'Good', '?']
Final General Boundary: [['BTech', '?', '?', '?'], ['?', '?', 'Good', '?']]
>>> 
