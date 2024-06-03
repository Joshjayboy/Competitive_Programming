async function updateProfile(name) {
  try {
    const response = await axios.post("/api/update-profile", { name });

    if (response.status !== 200) {
      // Handle HTTP error
      throw new Error("Failed to update profile");
    }

    return { success: true, data: response.data };
  } catch (error) {
    // Handle network error
    return { success: false, error: error.message };
  }
}
