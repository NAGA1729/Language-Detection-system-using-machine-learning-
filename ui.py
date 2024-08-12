{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "185135e1-3a9f-49e1-af9f-25d55502c2c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-08-12 17:48:22.394 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\nagav\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-08-12 17:48:22.405 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import string\n",
    "import streamlit as st\n",
    "import webbrowser\n",
    "\n",
    "global Lrdetect_Model\n",
    "\n",
    "LrdetectFile =open('project.pckl','rb')\n",
    "Lrdetect_Model=pickle.load(LrdetectFile)\n",
    "LrdetectFile.close()\n",
    "st.title(\"DETECT LANGUAGE\")\n",
    "\n",
    "input_test=st.text_input(\"Provide the input text to detect\",'Iam a CDACian')\n",
    "\n",
    "button_clicked=st.button(\"Get Language Name\")\n",
    "if button_clicked:\n",
    "    st.text(Lrdetect_Model.predict([input_test]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "null",
   "id": "161f237d-b90d-48c0-b68c-514c7a8255e4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
