import { useState } from 'react';

export default function App() {
  const [completed, setCompleted] = useState(false);

  return (
    <main className="shell">
      <section className="product" aria-labelledby="product-title">
        <p className="label">{{APP_TITLE}}</p>
        <h1 id="product-title">Replace this with the real product promise.</h1>
        <p className="intro">
          This neutral state proves the React starter runs. Delete it when implementing the actual core loop.
        </p>
        <button type="button" onClick={() => setCompleted(true)}>
          Try the core action
        </button>
        {completed && <p className="result">Replace this with the user's real useful result.</p>}
      </section>
    </main>
  );
}
