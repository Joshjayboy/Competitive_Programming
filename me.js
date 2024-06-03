function UpdateProfile({}) {
  const [name, setName] = useState("");
  const [error, setError] = useState(null);
  const [loading, startTransition] = useTransition();

  const handleSubmit = () => {
    startTransition(async () => {
      const error = await updateProfile(name);
      if (error) {
        setError(error);
        return;
      }
      redirect("/home");
    });
  };

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
