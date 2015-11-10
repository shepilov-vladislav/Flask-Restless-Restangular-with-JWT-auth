(function() {

    'use strict';

    angular
        .module('blogapp')
        .config(routeConfig)
        .run(routeRun)
        ;

    /** @ngInject */
    //routeConfig.$inject = ['$stateProvider', '$urlRouterProvider', '$authProvider'];
    function routeConfig($stateProvider, $urlRouterProvider, $authProvider) {
        $stateProvider
            .state('auth', {
                url: '/auth',
                templateUrl: 'static/app/auth/auth.html',
                controller: 'AuthController',
                controllerAs: 'auth'
            })
            .state('auth.login', {
                url: '/login',
                templateUrl: 'static/app/auth/login.html',
                controller: 'AuthController',
                controllerAs: 'auth',
                resolve: {
                    skipIfLoggedIn: skipIfLoggedIn
                }
            })
            .state('auth.register', {
                url: '/register',
                templateUrl: 'static/app/auth/register.html',
                controller: 'AuthController',
                controllerAs: 'auth'
            })
            .state('logout', {
                url: '/logout',
                controller: function($state, AuthService) {
                    AuthService.logout();
                    $state.go('auth.login');
                }
            })
            .state('article', {
                url: '/article',
                templateUrl: 'static/app/article/article.html',
                controller: 'ArticleController',
                controllerAs: 'article'
            })
            .state('home', {
                url: '/',
                templateUrl: 'static/app/main/main.html',
                controller: 'MainController',
                controllerAs: 'main'
            });

        $urlRouterProvider.otherwise('/');
        function skipIfLoggedIn($q, $auth) {
            var deferred = $q.defer();
            if ($auth.isAuthenticated()) {
                deferred.reject();
            } else {
                deferred.resolve();
            }
            return deferred.promise;
        }

        function loginRequired($q, $location, $auth) {
            var deferred = $q.defer();
            if ($auth.isAuthenticated()) {
                deferred.resolve();
            } else {
                $location.path('/login');
            }
            return deferred.promise;
        }

    }  // <-- routeConfig

    function routeRun($rootScope, $state, AuthService) {
        $rootScope.$on('$stateChangeStart', function(event, toState) {
            if (AuthService.getStorageMethod() == "localStorage") {
                var user = JSON.parse(localStorage.getItem('user'));
            } else {
                var user = JSON.parse(sessionStorage.getItem('user'));
            }

            if (user) {
                $rootScope.authenticated = true;
                $rootScope.currentUser = user;
                if(toState.name === "auth" || toState.name == "auth.login" || toState.name == "auth.register") {
                    event.preventDefault();
                    $state.go('article');
                }
            }
        });

    }  // <-- routeRun

})();
