import streamlit as st

st.set_page_config(page_title="Instructions", layout="wide")
st.title("📘 Instructions Page")
# Main section
st.write("Welcome to your personalized learning dashboard!")

# Add the 'How It Works' button
if st.button("📘 How the Recommendation System Works"):
    st.subheader("🧠 How the Recommendation System Works (For Everyone)")

    st.markdown("""
### 🔹 1. **Content-Based Filtering** (Recommends based on course content)

#### ✅ a. **Course Similarity Model**
- We read the **text of the courses** you've selected.
- Then, we find **other courses with similar words, topics, and themes**.
- It's like saying: "If you liked Course A because it was about Data Security, you'll probably like Course B because it's also about similar topics."

#### ✅ b. **User Profile Model**
- We look at the **topics covered** in the courses you chose.
- Your profile is built based on **those topics**.
- Then we find courses that **match your overall interest areas**.

---

### 🔹 2. **Clustering Model** (Recommends based on people like you)
- We compare your course preferences with **thousands of other users**.
- You are placed into a group (cluster) of people who like **similar kinds of courses**.
- We then show you **popular courses from your group**.

---

### 🔹 3. **Collaborative Filtering**

#### ✅ a. **KNN Model**
- We see how other users **rated the same courses** you liked.
- If many people who liked your courses also liked another one, we suggest it.

#### ✅ b. **NMF Model**
- We find **hidden patterns** in how you rate courses.
- Then, we recommend others that match those patterns—even if you haven’t seen them.

---

### 🔹 4. **Artificial Neural Network (ANN)**
- Uses advanced AI to learn your learning "personality".
- Gives highly personalized suggestions based on your unique behavior.

---

**In short**:  
Just select a few courses you've liked—and our system does the rest using smart AI methods!
""")

