""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class Surfer(CoreObject):
    """Generates surface mesh.

    Performs surface meshing using various surface meshing algorithms on topofaces or face zonelets.
    For example, constant size or volumetric size surface meshing.
    """

    def __init__(self, model: CommunicationManager, part_id: int):
        """ Initialize Surfer  """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Surfer/Construct"
        args = {"ModelID" : model._object_id , "PartID" : part_id, "MaxID" : -1}
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Surfer. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Surfer. """
        command_name = "PrimeMesh::Surfer/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def remesh_face_zonelets(self, face_zonelets : Iterable[int], edge_zonelets : Iterable[int], params : SurferParams) -> SurferResults:
        """ Performs meshing on the given face zonelets with provided parameters.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        edge_zonelets : Iterable[int]
            Ids of edge zonelets.
        params : SurferParams
            Surfer parameters.

        Returns
        -------
        SurferResults
            Returns the SurferResults.


        Examples
        --------
        >>> results = surfer.remesh_face_zonelets(face_zonelets, edge_zonelets, params)

        """
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(edge_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for edge_zonelets, valid argument type is Iterable[int].")
        if not isinstance(params, SurferParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SurferParams.")
        args = {"face_zonelets" : face_zonelets,
        "edge_zonelets" : edge_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Surfer/RemeshFaceZonelets"
        self._model._print_logs_before_command("remesh_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remesh_face_zonelets", SurferResults(model = self._model, json_data = result))
        return SurferResults(model = self._model, json_data = result)

    def mesh_topo_faces(self, topo_faces : Iterable[int], params : SurferParams) -> SurferResults:
        """ Performs meshing on the given topofaces with provided parameters.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topofaces.
        params : SurferParams
            Surfer Parameters.

        Returns
        -------
        SurferResults
            Returns the SurferResults.


        Examples
        --------
        >>> results = surfer.mesh_topo_faces(topo_faces, params)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for topo_faces, valid argument type is Iterable[int].")
        if not isinstance(params, SurferParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SurferParams.")
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Surfer/MeshTopoFaces"
        self._model._print_logs_before_command("mesh_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("mesh_topo_faces", SurferResults(model = self._model, json_data = result))
        return SurferResults(model = self._model, json_data = result)

    def initialize_surfer_params_for_wrapper(self) -> SurferParams:
        """ Initializes surfer parameters to mesh surfaces generated by wrapper.


        Returns
        -------
        SurferParams
            Returns the SurferParams initialized for wrapper inputs.


        Examples
        --------
        >>> surfer_params = surfer.initialize_surfer_params_for_wrapper()

        """
        args = {}
        command_name = "PrimeMesh::Surfer/InitializeSurferParamsForWrapper"
        self._model._print_logs_before_command("initialize_surfer_params_for_wrapper", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("initialize_surfer_params_for_wrapper", SurferParams(model = self._model, json_data = result))
        return SurferParams(model = self._model, json_data = result)

    def remesh_face_zonelets_locally(self, face_zonelets : Iterable[int], register_id : int, local_surfer_params : LocalSurferParams) -> LocalSurferResults:
        """ Remesh the given face zonelets locally at the registered faces with provided parameters.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Register id of the target faces.
        local_surfer_params : LocalSurferParams
            Local surfer Parameters.

        Returns
        -------
        LocalSurferResults
            Returns the LocalSurferResults.


        Examples
        --------
        >>> results = surfer.remesh_face_zonelets_locally(face_zonelets, register_id, local_surfer_params)

        """
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for register_id, valid argument type is int.")
        if not isinstance(local_surfer_params, LocalSurferParams):
            raise TypeError("Invalid argument type passed for local_surfer_params, valid argument type is LocalSurferParams.")
        args = {"face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "local_surfer_params" : local_surfer_params._jsonify()}
        command_name = "PrimeMesh::Surfer/RemeshFaceZoneletsLocally"
        self._model._print_logs_before_command("remesh_face_zonelets_locally", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remesh_face_zonelets_locally", LocalSurferResults(model = self._model, json_data = result))
        return LocalSurferResults(model = self._model, json_data = result)
