(function() {
    'use strict';
    angular
        .module('blogapp.article', [
            'restangular',
            'ngMessages',
            'angular-loading-bar'
        ])
        .config(function(RestangularProvider) {
            RestangularProvider.setBaseUrl('/api/v1');
            RestangularProvider.setResponseExtractor(function(response, operation) {
                var newResponse;
                if (operation === 'getList') {

                    newResponse = response.objects;
                    newResponse.metadata = {
                        numResults: response.num_results,
                        page: response.page,
                        totalPages: response.total_pages
                    };
                } else {
                    newResponse = response;
                }
                return newResponse;
            });
        });
})();
