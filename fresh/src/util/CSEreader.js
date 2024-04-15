import * as XLSX from 'xlsx';

export default function excelUpload(){
    const handleFileUpload = (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = (e) => {
            const data = new Uint8Array(e.target.result);
            const workbook = XLSX.read(data, {type : 'array'});

            const worksheet = workbook.Sheets[workbook.SheetNames[0]]

            const jsonData = XLSX.utils.sheet_to_json(worksheet, {header: 1});
            console.log(jsonData);

            

        };
        reader.readAsArrayBuffer(file);
    }
}