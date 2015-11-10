(function() {

    'use strict';

    angular
        .module('blogapp', [
            'ngAnimate',
            'ngCookies',
            'ngTouch',
            'ngSanitize',
            'restangular',
            'satellizer',
            'ui.router',
            'ui.bootstrap',
            'blogapp.auth',
            'blogapp.article'
        ]);

})();
