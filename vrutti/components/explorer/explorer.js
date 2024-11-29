function openFile() {
    window.electronAPI.openDialog({
        properties: ['openFile']
    }).then(result => {
        if (!result.canceled) {
            populateFileList(result.filePaths);
        }
    }).catch(err => console.log(err));
}

function openFolder() {
    window.electronAPI.openDialog({
        properties: ['openDirectory']
    }).then(result => {
        if (!result.canceled) {
            populateFileList(result.filePaths);
        }
    }).catch(err => console.log(err));
}
