import { useState } from 'react';
import './index.css';

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [processedFile, setProcessedFile] = useState<string>('');

  function changeFile(event: React.ChangeEvent<HTMLInputElement>) {
    setFile(event.target.files![0]);
  }

  async function uploadPayroll(event: React.FormEvent) {
    if (file === null) return;

    event.preventDefault();

    const url: string = 'http://127.0.0.1:5000/upload_payroll';

    const payrollForm: FormData = new FormData();
    payrollForm.append('file', file!);

    const payrollProcessorResponse: any = await fetch(url, {
      method: 'POST',
      body: payrollForm,
    });

    const processedPayroll: any = await payrollProcessorResponse.blob();
    setProcessedFile(window.URL.createObjectURL(processedPayroll));
  }

  return (
    <>
      <form className='fileUpload'>
        <div>upload payroll</div>
        <input type='file' onChange={changeFile} />
        <button type='submit' onClick={uploadPayroll}>upload</button>
      </form>
      <div className='download'>
        {processedFile !== '' && <a href={processedFile} download={'processed_payroll.csv'}>download</a>}
      </div>
    </>
  )
}

export default App
