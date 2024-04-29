import streamlit as st
import numpy as np
import joblib 
import os

trueOrFalse = {'0': False, '1': True}

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

def get_values(val,my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value
        
@st.cache_data
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),'rb'))
    return loaded_model

        
def run_ml_app():
    manufacturer = st.selectbox("MANUFACTURE", ['Hyundai', 'Toyota', 'Mercedes-Benz', 'Chevrolet', 'Honda', 
                    'Ford', 'BMW', 'Others', 'Nissan', 'Ssangyong', 
                    'Volkswagen', 'KIA', 'Lexus', 'Mitsubishi', 'Opel', 
                    'Subaru', 'Audi', 'Jeep', 'Mazda'])
    production_year = st.selectbox("TAHUN", ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
    category = st.selectbox("CATEGORY", ['Sedan', 'Jeep', 'Hatchback', 'Minivan', 'Coupe', 'Universal', 'Microbus', 'Goods wagon', 'Pickup', 'Cabriolet',
                                                'Limousine'])
    leather_interior = st.selectbox("Leather interior", ['0', '1'])
    fuel_type = st.selectbox("Fuel type", ['Petrol', 'Diesel', 'Hybrid', 'LPG', 'CNG', 'Plug-in-Hybrid', 'Hydrogen'])
    engine_volume = st.number_input("Engine volume")
    mileage = st.number_input("Mile age")
    gear_box_type = st.selectbox("Gear box type", ['Automatic', 'Triptonic', 'Manual', 'Variator'])
    drive_wheels = st.selectbox("Drive wheels", ['All', 'Front', 'Rear'])
    color = st.selectbox("Color", ['Black', 'White', 'Silver', 'Grey', 'Blue', 'Red', 'Carnelian red', 'Green',
                                   'Brown', 'Golden', 'Sky Blue', 'Beige', 'Yellow', 'Orange', 'Purple', 'Pink'])
    left_wheel = st.selectbox("left wheel", ['0', '1'])

    with st.expander("Your Selected Options"):
        result = {
            'manufacturer':manufacturer,
            'production_year':production_year,
            'category':category, 
            'leather_interior':leather_interior,
            'fuel_type':fuel_type,
            'engine_volume':engine_volume,
            'mileage':mileage,
            'gear_box_type':gear_box_type,
            'drive_wheels':drive_wheels,
            'color':color,
            'left_wheel':left_wheel,
        }
    
    #st.write(result)

    encoded_result = []
    for i in result.values():
        if type(1) == int:
            encoded_result.append(i)
        elif i in ["0", "1"]:
            encoded_result.append(get_values(i, trueOrFalse))

    # st.write(encoded_result)

    ## prediction section
    st.subheader('prediction Result')

    #Decode
    single_sample = np.array(encoded_result).reshape(1,-1)
    # st.write(single_Sample)

    model = load_model("model_grad.pkl")

    prediction = model.predict(single_sample)
    st.write(prediction)




