#include <QApplication>
#include <QWidget>
#include <QVBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QStyle>
#include <QInputDialog>
#include <QMessageBox>
#include <QTextEdit>
#include <QHBoxLayout>
#include <QProcess>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    // Create the main window
    QWidget window;
    window.setWindowTitle("Protector Security Suite - C++ Engine");
    window.resize(450, 400);

    // Layout management
    QVBoxLayout *layout = new QVBoxLayout(&window);

    // UI Elements
    QLabel *titleLabel = new QLabel("🛡️ Protection Dashboard");
    titleLabel->setStyleSheet("font-size: 20px; font-weight: bold;");
    
    QLabel *statusLabel = new QLabel("Status: System Active & Monitoring");
    statusLabel->setStyleSheet("color: green;");

    QPushButton *blockBtn = new QPushButton("Manually Block IP");
    QPushButton *logBtn = new QPushButton("View Security Logs");

    QTextEdit *logView = new QTextEdit();
    logView->setReadOnly(true);
    logView->append("Security logs will appear here.");

    QProcess *process = new QProcess(&window);

    // Adding elements to the layout
    layout->addWidget(titleLabel);
    layout->addWidget(statusLabel);
    layout->addSpacing(20);
    layout->addWidget(blockBtn);
    layout->addWidget(logBtn);
    layout->addWidget(logView);

    window.show();

    // Connect signals
    QObject::connect(blockBtn, &QPushButton::clicked, [&]() {
        bool ok;
        QString ip = QInputDialog::getText(&window, "Block IP", "Enter IP address to block:", QLineEdit::Normal, "", &ok);
        if (ok && !ip.isEmpty()) {
            process->setWorkingDirectory("../python");
            QString command = QString("from protector import IPBlocker; b = IPBlocker(); b.block_ip('%1'); print('Blocked %1')").arg(ip);
            process->start("python", QStringList() << "-c" << command);
            if (process->waitForFinished(5000)) {  // Wait up to 5 seconds
                QString output = process->readAllStandardOutput();
                logView->append(output.trimmed());
                QMessageBox::information(&window, "Blocked", QString("IP %1 has been blocked.").arg(ip));
            } else {
                QMessageBox::warning(&window, "Error", "Failed to block IP: " + process->errorString());
            }
        }
    });

    QObject::connect(logBtn, &QPushButton::clicked, [&]() {
        logView->append("Viewing security logs...");
        // In a real app, load logs from file
    });

    return app.exec();
}