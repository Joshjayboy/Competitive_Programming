function UpdateProfile({}) {
  const [name, setName] = useState("");
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    const error = await updateProfile(name);
    setLoading(false);

    if (error) {
      setError(error);
      return;
    }
  };

  redirect("/home");
  return (
    <div>
      <input value={name} onChange={(event) => setName(event.target.value)} />
      <button onClick={handleSubmit} disabled={loading}>
        Update
      </button>
      {error && <p>{error}</p>}
    </div>
  );
}
