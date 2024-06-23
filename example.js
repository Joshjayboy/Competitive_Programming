import React, { useState, useEffect } from "react";

const InputField = () => {
  const [inputValue, setInputValue] = useState("");

  const LOCAL_STORAGE_KEY = "example";

  //   Retrieve the value from local storage
  useEffect(() => {
    const storedValue = localStorage.getItem(LOCAL_STORAGE_KEY);
    if (storedValue) {
      setInputValue(storedValue);
    }
  }, []);

  //   Save the value to local storage
  const handleInputChange = (e) => {
    const value = e.target.value;
    setInputValue(e.target.value);
    localStorage.setItem(LOCAL_STORAGE_KEY, value);
  };
  return (
    <div>
      <textarea
        value={inputValue}
        onChange={handleInputChange}
        placeholder="Type something..."
        rows="10"
        cols="30"
      />
    </div>
  );
};

export default InputField;
