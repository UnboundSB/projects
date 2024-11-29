// main.js
const { app, BrowserWindow, ipcMain, dialog } = require("electron");

let mainWindow;

app.on("ready", () => {
    mainWindow = new BrowserWindow({
        webPreferences: {
            preload: `${__dirname}/preload.js`,
            contextIsolation: true,
            nodeIntegration: false
        }
    });

    mainWindow.loadFile("index.html");
});

ipcMain.handle("dialog:open", async () => {
    const result = await dialog.showOpenDialog({
        properties: ["openFile", "openDirectory", "multiSelections"]
    });
    return result.filePaths;
});
