# Import Libraries
from owlready2 import *
import streamlit as st


 onto_path = "path/to/your/math_ontology.owl"  
 onto = get_ontology(onto_path).load()  


#Data for Shapes, Formulas, and Answers

hardcoded_data = {
    "Circle": {
        "formula": "π × radius × radius",
        "explanation": "To calculate the area of a circle, multiply π (3.14) by the radius squared.",
        "answers": {1: 3.14, 2: 12.57, 3: 28.27, 4: 50.27, 5: 78.54, 6: 113.10, 7: 153.94, 8: 201.06, 9: 254.47, 10: 314.16}
    },
    "Square": {
        "formula": "side × side",
        "explanation": "To calculate the area of a square, multiply the length of the side by itself.",
        "answers": {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    },
    "Rectangle": {
        "formula": "length × width",
        "explanation": "To calculate the area of a rectangle, multiply the length by the width.",
        "answers": {1: 1, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}
    },
    "Triangle": {
        "formula": "0.5 × base × height",
        "explanation": "To calculate the area of a triangle, multiply 0.5 by the base and height.",
        "answers": {1: 0.5, 2: 2, 3: 4.5, 4: 8, 5: 12.5, 6: 18, 7: 24.5, 8: 32, 9: 40.5, 10: 50}
    },
    "Cube": {
        "formula": "6 × side × side",
        "explanation": "To calculate the surface area of a cube, multiply 6 by the square of the side length.",
        "answers": {1: 6, 2: 24, 3: 54, 4: 96, 5: 150, 6: 216, 7: 294, 8: 384, 9: 486, 10: 600}
    },
    "Pyramid": {
        "formula": "1/3 × base area × height",
        "explanation": "To calculate the volume of a pyramid, multiply 1/3 by the base area and height.",
        "answers": {1: 0.33, 2: 1.33, 3: 3, 4: 5.33, 5: 8.33, 6: 12, 7: 16.33, 8: 21.33, 9: 27, 10: 33.33}
    }
}


st.set_page_config(page_title="Math ITS - Shapes & Formulas", layout="wide")
st.title("🧠 Intelligent Tutoring System for Math")
st.write("Learn and calculate areas or volumes for different shapes!")

# Dropdown to Select Shape
shape = st.selectbox("Select a Shape", list(hardcoded_data.keys()))

# Input Value
value = st.number_input("Enter a Value (1-10):", min_value=1, max_value=10, step=1)

# Display Formula and Explanation
st.subheader("Formula and Explanation")
st.write(f"**Formula:** {hardcoded_data[shape]['formula']}")
st.write(f"**Explanation:** {hardcoded_data[shape]['explanation']}")

# Calculate Area or Volume
if st.button("Calculate"):
    result = hardcoded_data[shape]["answers"].get(value, "N/A")
    st.success(f"The calculated value for {shape} with input {value} is: **{result}**")


 OWL Integration 

 def get_owl_data(shape):  
     formulas = []  
    for instance in onto[shape].instances(): 
         if hasattr(instance, "hasFormula"):  
             formulas.append(instance.hasFormula[0])  
     return formulas  

 if st.button("Load OWL Data"):  
     owl_formulas = get_owl_data(shape)  
     if owl_formulas:  
         st.subheader("Formulas from OWL File") 
         for formula in owl_formulas:  
             st.write(f"- {formula}")  
     else:  
         st.error("No formulas found for this shape in the OWL file.") 


import streamlit as st


# Data for Shapes, Formulas, and Predefined Results

hardcoded_data = {
    "Circle": {
        "Formula": "π × radius × radius",
        "Values": [1, 2, 3, 4, 5],
        "Results": {1: 3.14, 2: 12.56, 3: 28.26, 4: 50.24, 5: 78.5}
    },
    "Square": {
        "Formula": "side × side",
        "Values": [1, 2, 3, 4, 5],
        "Results": {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    },
    "Triangle": {
        "Formula": "0.5 × base × height",
        "Values": ["3,4", "6,8"],
        "Results": {"3,4": 6.0, "6,8": 24.0}
    },
    "Rectangle": {
        "Formula": "length × width",
        "Values": ["3,5", "6,4"],
        "Results": {"3,5": 15.0, "6,4": 24.0}
    },
    "Cube": {
        "Formula": "6 × side²",
        "Values": [1, 2, 3],
        "Results": {1: 6, 2: 24, 3: 54}
    },
    "Pyramid": {
        "Formula": "1/3 × base area × height",
        "Values": ["9,3"],
        "Results": {"9,3": 9.0}
    }
}



# Operations


# Data for Shapes and Formulas
hardcoded_data = {
    "Circle": {
        "Formula": "π × radius × radius",
        "Example Input": [1, 2, 3, 4, 5],
        "Results": {1: 3.14, 2: 12.56, 3: 28.26, 4: 50.24, 5: 78.5}
    },
    "Square": {
        "Formula": "side × side",
        "Example Input": [1, 2, 3, 4, 5],
        "Results": {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    },
    "Triangle": {
        "Formula": "0.5 × base × height",
        "Example Input": [(3, 4), (6, 8)],
        "Results": {"3,4": 6.0, "6,8": 24.0}
    },
    "Rectangle": {
        "Formula": "length × width",
        "Example Input": [(3, 5), (6, 4)],
        "Results": {"3,5": 15.0, "6,4": 24.0}
    },
    "Cube": {
        "Formula": "6 × side²",
        "Example Input": [1, 2, 3],
        "Results": {1: 6, 2: 24, 3: 54}
    },
    "Pyramid": {
        "Formula": "1/3 × base area × height",
        "Example Input": [(9, 3)],
        "Results": {"9,3": 9.0}
    }
}

# Function to Perform Operations
def perform_operation(shape, operation, values):
    if operation == "Addition":
        return sum(values)
    elif operation == "Multiplication":
        result = 1
        for v in values:
            result *= v
        return result
    elif operation == "Division":
        try:
            result = values[0]
            for v in values[1:]:
                result /= v
            return result
        except ZeroDivisionError:
            return "Error: Division by Zero"
    elif operation == "Subtraction":
        result = values[0]
        for v in values[1:]:
            result -= v
        return result
    return "Unknown Operation"



st.write("---")
st.header(" Perform Advanced Operations on Shapes")

# Shape and Operation Selection
shape = st.selectbox("Select a Shape", list(hardcoded_data.keys()), key="shape_interactive")
operation = st.selectbox("Select an Operation", ["Addition", "Multiplication", "Division", "Subtraction"], key="operation_selection")

# Input and Calculation Section
st.subheader(f" Formula for {shape}: {hardcoded_data[shape]['Formula']}")
if shape in ["Circle", "Square", "Cube"]:
    value = st.number_input("Enter a Single Value:", min_value=1, max_value=5, step=1)
    if value:
        result = hardcoded_data[shape]["Results"].get(value, "No Predefined Result")
        st.success(f"The calculated result: {result}")
        st.write(f"### Explanation: {hardcoded_data[shape]['Formula']} → {result}")
elif shape in ["Triangle", "Rectangle", "Pyramid"]:
    values = st.text_input("Enter Dimensions as Comma-Separated Values (e.g., 3,4):")
    if values:
        try:
            key = ",".join(values.strip().split(","))
            result = hardcoded_data[shape]["Results"].get(key, "No Predefined Result")
            st.success(f"The calculated result: {result}")
            st.write(f"### Explanation: {hardcoded_data[shape]['Formula']} → {result}")
        except:
            st.error("Invalid Input Format! Please enter values correctly.")

import streamlit as st


# Shapes, Operations, and Results

hardcoded_data = {
    "Circle": {
        "Formula": "π × radius × radius",
        "Operations": ["Multiplication"],
        "Values": [1, 2, 3, 4, 5],
        "Results": {1: 3.14, 2: 12.56, 3: 28.26, 4: 50.24, 5: 78.5}
    },
    "Square": {
        "Formula": "side × side",
        "Operations": ["Multiplication"],
        "Values": [1, 2, 3, 4, 5],
        "Results": {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    },
    "Triangle": {
        "Formula": "0.5 × base × height",
        "Operations": ["Multiplication"],
        "Values": ["3,4", "6,8"],
        "Results": {"3,4": 6.0, "6,8": 24.0}
    },
    "Rectangle": {
        "Formula": "length × width",
        "Operations": ["Multiplication"],
        "Values": ["3,5", "6,4"],
        "Results": {"3,5": 15.0, "6,4": 24.0}
    },
    "Cube": {
        "Formula": "6 × side²",
        "Operations": ["Multiplication"],
        "Values": [1, 2, 3],
        "Results": {1: 6, 2: 24, 3: 54}
    },
    "Pyramid": {
        "Formula": "1/3 × base area × height",
        "Operations": ["Multiplication"],
        "Values": ["9,3"],
        "Results": {"9,3": 9.0}
    }
}


# ---------------------------
# Notes Section
# ---------------------------
st.info("This Intelligent Tutoring System allows you to explore formulas, operations, and properties for different shapes!")

# ---------------------------
#Future 
# ---------------------------
st.write("---")
st.write("### Future Developments:")
st.write("1. **AI-Powered Adaptive Learning** - The system adapts difficulty levels based on user performance using machine learning.")
st.write("2. **Voice-Controlled Interface** - Interact with the system using voice commands to query shapes and formulas.")
st.write("3. **Real-Time 3D Visualization** - Render 3D models of shapes with dynamic formulas and inputs.")
st.write("4. **Augmented Reality (AR) Integration** - Project shapes and formulas into the real world using AR devices.")
st.write("5. **Natural Language Question Answering** - Allow users to ask shape-related questions in plain English and get accurate formula explanations.")
st.write("6. **Gamified Learning Modules** - Include quizzes, rewards, and interactive challenges to boost user engagement.")
st.write("7. **Advanced Analytics Dashboard** - Provide detailed reports on user progress, errors, and learning pace.")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.write("📌 **Developed to run the OWL for AI assignment in MSc Computer Science at YSJU.**")
