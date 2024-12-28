use std::process::{Command, Child};
use tauri::{Manager};
use std::sync::Mutex;

fn start_flask_backend() -> std::process::Child {
    std::process::Command::new("./bin/app")
        .spawn()
        .unwrap_or_else(|err| panic!("Failed to start Flask backend at {path}: {err}"))
}



pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let flask_child = start_flask_backend();

            app.manage(Mutex::new(flask_child));

            Ok(())
        })
        .on_window_event(|_window, event| {
            if let tauri::WindowEvent::CloseRequested { .. } = event {
                if let Ok(mut child) = _window.state::<Mutex<Child>>().lock() {
                    let _ = child.kill();
                }
            }
        })
        .run(tauri::generate_context!())
        .expect("error while running Tauri application");
}
