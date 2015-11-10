(function() {

    'use strict';

    angular
        .module('blogapp.auth')
        .factory('AuthService', AuthService);

    AuthService.$inject = ['$auth', '$state', '$http', 'API', '$rootScope', '$q'];
    function AuthService($auth, $state, $http, API, $rootScope, $q) {
        var Auth = {
            register: register,
            login: login,
            logout: logout,
            saveUser: saveUser,
            getStorageMethod: getStorageMethod,
            regStatus: null,
            regStatusMessage: null,
            registered: null,
            storageMethod: 'localStorage',
            isAuthenticated: isAuthenticated,
            getCurrentStorageMethod: getCurrentStorageMethod,
            getUser: getUser,
            getUID: getUID
        };

        return Auth;

        function register(email, username, password) {
            return $http.post(API + '/users/', {
                email: email,
                username: username,
                password: password
            });
        }

        function saveUser(user) {
            $http.get(API+'/api/v1/user/'+user.user_id).then(function(userResponse) {
              var userString = JSON.stringify(userResponse.data);
              if (Auth.storageMethod == "localStorage") {
                  localStorage.setItem("user", userString);
              } else {
                  sessionStorage.setItem("user", userString);
              }
              $rootScope.authenticated = true;
              $rootScope.currentUser = userResponse.data;
            });
        }

        function login(credentials, remember_me) {
            if (remember_me == true) {
                Auth.storageMethod = 'localStorage';
            } else {
                Auth.storageMethod = 'sessionStorage';
            }

            $auth.setStorageType(this.storageMethod);
            var deferred = $q.defer();
            $auth.login(credentials).then(function(response) {
                var user = $auth.getPayload();
                deferred.resolve(user);
            }, function(response) {
                return deferred.reject(response);
            });

            return deferred.promise;
        }

        function logout() {
            $auth.logout().then(function() {
                localStorage.removeItem('user');
                $rootScope.authenticated = false;
                $rootScope.currentUser = null;
            });
        }

        function getStorageMethod() {
            return Auth.storageMethod;
        }

        function getCurrentStorageMethod(){
            var storage_method = null;
            if (Auth.storageMethod === 'localStorage') {
                storage_method = localStorage;
            }
            else if (Auth.storageMethod === 'sessionStorage') {
                storage_method = sessionStorage;
            }
            else { throw "Unknown storageMethod!"; }
            return storage_method;
        }

        function isAuthenticated() {
            return $rootScope.authenticated;
        }

        function getUser() {
            var current_user = null;
            if (isAuthenticated()) {
                var current_user = angular.fromJson(getCurrentStorageMethod().getItem("user"));
            }
            return current_user;
        }

        function getUID() {
            var result;
            var current_user = getUser();
            if (current_user !== null) {
                result = current_user["id"];
            }
            else {
                result = undefined;
            }
            return result;
        }

    }  // <-- AuthService

})();
