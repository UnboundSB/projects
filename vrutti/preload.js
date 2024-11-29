const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("electronAPI", {
    openDialog: () => ipcRenderer.invoke("dialog:open")
});



// Expose the Open Folder functionality to the renderer
contextBridge.exposeInMainWorld('electron', {
    openFolderDialog: () => ipcRenderer.send('open-folder-dialog'),
    onFolderSelected: (callback) => ipcRenderer.on('folder-selected', callback),
});

contextBridge.exposeInMainWorld('electron',{
    openFileDialog: () => ipcRenderer.send('open-file-dialog'),
    onFileSelected: () => ipcRenderer.on('file-selected', callback),
});
