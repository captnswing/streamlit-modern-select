import React from "react"
import ReactDOM from "react-dom/client"
import ModernSelect from "./ModernSelect"

const rootElement = document.getElementById('root');
if (!rootElement) throw new Error('Failed to find the root element');

const root = ReactDOM.createRoot(rootElement);

root.render(
    <React.StrictMode>
        <ModernSelect/>
    </React.StrictMode>,
)
