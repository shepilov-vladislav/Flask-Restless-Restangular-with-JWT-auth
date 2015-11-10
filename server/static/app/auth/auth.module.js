(function() {

    'use strict';
    angular
        .module('blogapp.auth', [
            'satellizer',
            'ui.router',
            'ngMessages'
        ]).constant('API', '')
        .config(function($authProvider) {
            $authProvider.loginUrl = '/auth';
            $authProvider.signupUrl = '/users';
        });

})();
