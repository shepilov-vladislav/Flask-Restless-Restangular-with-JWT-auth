(function() {
    'use strict';

    angular
        .module('blogapp.auth')
        .directive('uniqueUsername', uniqueUsername);

    uniqueUsername.$inject = ['API', '$http'];
    function uniqueUsername(API, $http) {
        var uniqueUsernameDirective = {
            require: 'ngModel',
            restrict: 'EA',
            link: linkFunc
        };

        return uniqueUsernameDirective;

        /** @ngInject */
        function linkFunc(scope, el, attr, ngModel) {
            var url = API + '/users/username';

            ngModel.$parsers.push(function(val) {
                if (!val || val.length == 0) {
                    return;
                }
                ngModel.$setValidity('usernameAvailability', false);

                var data = {username: val};

                $http.post(url, data)
                .then(function(response) {
                    ngModel.$setValidity('usernameAvailability', true);
                }, function(response) {
                    ngModel.$setValidity('usernameAvailability', false);
                });
                return val;
            });
        }

    }  // <-- uniqueUsername

})();
