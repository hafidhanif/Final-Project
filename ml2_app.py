import streamlit as st
import numpy as np

#load ML package
# import joblib
# import os

attribute_info = """"
                - manufacturer
                - production year
                - category
                - leather interior
                - fuel type
                - engine volume
                - mileage
                - gear_box_type
                - drive_wheels
                - color
                - left wheel
                """

# production_year = {'2000':, '2001':,'2002':, '2003':'2004':, '2005':'2006':, '2007':'2008':, '2009':,
#                    '2010':, '2011':,'2012':, '2013':'2014':, '2015':'2016':, '2017':'2018':, '2019':,'2020':}
# category = {'Coupe':, 'Goods Wagon':, 'Hatchback':, 'Jeep':, 'Limousin':, 'Microbus':, 'Minivan':, 'Pickup':, 'Sedan':, 'Universal':}
# leather_interior = {'0':, '1':}
# fuel_type = {'Diesel':, 'Hybrid':, 'Hydrogen':, 'LPG':, 'Petrol':, 'Plug-in Hybrid':}
# engine_volume = {'0':, '1':}
# mileage = {}
# gear_box_type = {}
# drive_wheels = {}
# color = {}
# left wheel = {}
def run_ml2_app():
    manufacturer = st.selectbox("MANUFAKTUR", ['Hyundai', 'Toyota', 'Mercedes-Benz', 'Chevrolet', 'Honda', 
                    'Ford', 'BMW', 'Others', 'Nissan', 'Ssangyong', 
                    'Volkswagen', 'KIA', 'Lexus', 'Mitsubishi', 'Opel', 
                    'Subaru', 'Audi', 'Jeep', 'Mazda'])
    production_year = st.selectbox("TAHUN", ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                                                '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
    category = "Jeep"
    leather_interior = 1   # True= 1 and False= 0
    fuel_type = "Hybrid"
    engine_volume = 3.5
    mileage = 186005
    gear_box_type = "Automatic"
    drive_wheels = "All"
    color = "Silver"
    left_wheel = 1   # True= 1 and False= 0



