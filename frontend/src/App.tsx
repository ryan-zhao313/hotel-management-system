import { useState } from 'react';
import './index.css';

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<string>('');

  function changeFile(event: React.ChangeEvent<HTMLInputElement>) {
    setFile(event.target.files![0]);
  }

  async function uploadFile(event: React.FormEvent) {
    event.preventDefault();

    const url: string = 'http://127.0.0.1:5000/upload';

    const formData: FormData = new FormData();
    formData.append('file', file!);

    const response: any = await fetch(url, {
      method: 'POST',
      body: formData,
    });

    const data: any = await response.json();
    setResult(data.data);
  }

  return (
    <>
      <form className='fileUpload'>
        <p>upload csv</p>
        <input type='file' onChange={changeFile} />
        <button type='submit' onClick={uploadFile}>upload</button>
      </form>
      <div className='result'>{result}</div>
    </>
  )
}

export default App
