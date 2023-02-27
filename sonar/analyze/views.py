from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .neo4j_analysis_client import Neo4jAnalysisClient

class RequestValidator():

    def validate(self, required_fields):

        if None in required_fields.values():
            missing_fields = [field_name for field_name in required_fields.keys() if required_fields.get(field_name) is None]
            return Response({'error': 'missing form fields: ' + str(missing_fields)}, status=status.HTTP_400_BAD_REQUEST)

        return None

class BetweennessCentralityView(APIView):

    permission_classes = (IsAuthenticated,)
    neo4j_analysis_client = Neo4jAnalysisClient()
    request_validator = RequestValidator()

    def get(self, request):

        user = request.user
        
        node_type = request.query_params.get('node_type')
        edge_type = request.query_params.get('edge_type')

        print(node_type, edge_type)

        fields = {
            'node_type': node_type,
            'edge_type': edge_type
        }

        validation_result = self.request_validator.validate(fields)

        if validation_result:
            return validation_result
        
        homogenous_node_edge_pairs = [
            ("Author", "Coauthorship"),
            ("Article", "Cites")
        ]

        if node_type not in [pair[0] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid node type'}, status=status.HTTP_400_BAD_REQUEST)
        
        print(homogenous_node_edge_pairs[:][1])
        
        if edge_type not in [pair[1] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid edge type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if (node_type, edge_type) not in homogenous_node_edge_pairs:
            return Response({'error': 'invalid node type and edge type combination'}, status=status.HTTP_400_BAD_REQUEST)

        betweenness = self.neo4j_analysis_client.calculate_betweenness_centrality(user.username, node_type, edge_type)

        return Response(betweenness, status=status.HTTP_200_OK)
    
class ClosenessCentralityView(APIView):

    permission_classes = (IsAuthenticated,)
    neo4j_analysis_client = Neo4jAnalysisClient()
    request_validator = RequestValidator()

    def get(self, request):

        user = request.user
        
        node_type = request.query_params.get('node_type')
        edge_type = request.query_params.get('edge_type')

        fields = {
            'node_type': node_type,
            'edge_type': edge_type
        }

        validation_result = self.request_validator.validate(fields)

        if validation_result:
            return validation_result
        
        homogenous_node_edge_pairs = [
            ("Author", "Coauthorship"),
            ("Article", "Cites")
        ]

        if node_type not in [pair[0] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid node type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if edge_type not in [pair[1] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid edge type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if (node_type, edge_type) not in homogenous_node_edge_pairs:
            return Response({'error': 'invalid node type and edge type combination'}, status=status.HTTP_400_BAD_REQUEST)

        closeness = self.neo4j_analysis_client.calculate_closeness_centrality(user.username, node_type, edge_type)

        return Response(closeness, status=status.HTTP_200_OK)
    
class EigenvectorCentralityView(APIView):

    permission_classes = (IsAuthenticated,)
    neo4j_analysis_client = Neo4jAnalysisClient()
    request_validator = RequestValidator()

    def get(self, request):

        user = request.user
        
        node_type = request.query_params.get('node_type')
        edge_type = request.query_params.get('edge_type')

        fields = {
            'node_type': node_type,
            'edge_type': edge_type
        }

        validation_result = self.request_validator.validate(fields)

        if validation_result:
            return validation_result
        
        homogenous_node_edge_pairs = [
            ("Author", "Coauthorship"),
            ("Article", "Cites")
        ]

        if node_type not in [pair[0] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid node type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if edge_type not in [pair[1] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid edge type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if (node_type, edge_type) not in homogenous_node_edge_pairs:
            return Response({'error': 'invalid node type and edge type combination'}, status=status.HTTP_400_BAD_REQUEST)

        eigenvector = self.neo4j_analysis_client.calculate_eigenvector_centrality(user.username, node_type, edge_type)

        return Response(eigenvector, status=status.HTTP_200_OK)
    
class DegreeCentralityView(APIView):

    permission_classes = (IsAuthenticated,)
    neo4j_analysis_client = Neo4jAnalysisClient()
    request_validator = RequestValidator()

    def get(self, request):

        user = request.user
        
        node_type = request.query_params.get('node_type')
        edge_type = request.query_params.get('edge_type')

        fields = {
            'node_type': node_type,
            'edge_type': edge_type
        }

        validation_result = self.request_validator.validate(fields)

        if validation_result:
            return validation_result
        
        homogenous_node_edge_pairs = [
            ("Author", "Coauthorship"),
            ("Article", "Cites")
        ]

        if node_type not in [pair[0] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid node type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if edge_type not in [pair[1] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid edge type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if (node_type, edge_type) not in homogenous_node_edge_pairs:
            return Response({'error': 'invalid node type and edge type combination'}, status=status.HTTP_400_BAD_REQUEST)

        degree = self.neo4j_analysis_client.calculate_degree_centrality(user.username, node_type, edge_type)

        return Response(degree, status=status.HTTP_200_OK)
    
class PageRankView(APIView):

    permission_classes = (IsAuthenticated,)
    neo4j_analysis_client = Neo4jAnalysisClient()
    request_validator = RequestValidator()

    def get(self, request):

        user = request.user
        
        node_type = request.query_params.get('node_type')
        edge_type = request.query_params.get('edge_type')

        fields = {
            'node_type': node_type,
            'edge_type': edge_type
        }

        validation_result = self.request_validator.validate(fields)

        if validation_result:
            return validation_result
        
        homogenous_node_edge_pairs = [
            ("Author", "Coauthorship"),
            ("Article", "Cites")
        ]

        if node_type not in [pair[0] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid node type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if edge_type not in [pair[1] for pair in homogenous_node_edge_pairs]:
            return Response({'error': 'invalid edge type'}, status=status.HTTP_400_BAD_REQUEST)
        
        if (node_type, edge_type) not in homogenous_node_edge_pairs:
            return Response({'error': 'invalid node type and edge type combination'}, status=status.HTTP_400_BAD_REQUEST)

        page_rank = self.neo4j_analysis_client.calculate_pagerank(user.username, node_type, edge_type)

        return Response(page_rank, status=status.HTTP_200_OK)