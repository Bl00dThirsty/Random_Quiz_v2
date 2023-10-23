module.exports = {
  apps: [
    {
      name: 'apps.quiz',
      script: 'manage.py',
      args: 'runserver 192.168.1.68:8000',
      interpreter: 'python3',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '1G',
      env: {
        DJANGO_SETTINGS_MODULE: 'Random.settings',
      },
    },
  ],
};
