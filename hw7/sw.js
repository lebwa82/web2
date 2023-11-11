self.addEventListener('install', (event) => {
    console.log('Service Worker installed.');
});

self.addEventListener('push', (event) => {
    const title = "New Message";
    const options = {
        body: event.data.text(),
    };

    event.waitUntil(self.registration.showNotification(title, options));
});