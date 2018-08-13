from enum import Enum
from ontology.smart_contract.neo_contract.abi.abi_function import AbiFunction
from ontology.vm.op_code import PACK
from ontology.vm.params_builder import ParamsBuilder


class BuildParams(object):
    class Type(Enum):
        bytearraytype = 0x00
        booltype = 0x01
        integertype = 0x02
        arraytype = 0x80
        structtype = 0x81
        maptype = 0x82

    @staticmethod
    def serialize_abi_function(abi_func: AbiFunction):
        param_list = []
        param_list.append(bytes(abi_func.name.encode()))
        temp_list = []
        for param in abi_func.parameters:
            temp_list.append(param.value)
        param_list.append(temp_list)
        return BuildParams.create_code_params_script(param_list)

    @staticmethod
    def create_code_params_script(param_list: [])->bytearray:
        builder = ParamsBuilder()
        length = len(param_list)
        for j in range(length):
            i = length - 1 - j
            if isinstance(param_list[i], bytearray) or isinstance(param_list[i], bytes):
                builder.emit_push_byte_array(param_list[i])
            elif isinstance(param_list[i], str):
                builder.emit_push_byte_array(str.encode(param_list[i]))
            elif isinstance(param_list[i], int):
                builder.emit_push_integer(param_list[i])
            elif isinstance(param_list[i], bool):
                builder.emit_push_bool(param_list[i])
            elif isinstance(param_list[i], dict):
                # TODO
                builder.emit_push_byte_array(BuildParams.get_map_bytes())
            elif isinstance(param_list[i], list):
                BuildParams.create_code_params_script_builder(param_list[i], builder)
                print(builder.to_array().hex())
                builder.emit_push_integer(len(param_list[i]))
                builder.emit(PACK)
        return bytearray(builder.to_array())

    @staticmethod
    def create_code_params_script_builder(param_list: [], builder: ParamsBuilder):
        length = len(param_list)
        for j in range(length):
            i = length - 1 - j
            if isinstance(param_list[i], bytearray) or isinstance(param_list[i], bytes):
                builder.emit_push_byte_array(param_list[i])
            elif isinstance(param_list[i], str):
                builder.emit_push_byte_array(bytes(param_list[i].encode()))
            elif isinstance(param_list[i], int):
                builder.emit_push_integer(param_list[i])
            elif isinstance(param_list[i], bool):
                builder.emit_push_bool(param_list[i])
            elif isinstance(param_list[i], dict):
                # TODO
                builder.emit_push_byte_array(BuildParams.get_map_bytes())
            elif isinstance(param_list[i], list):
                BuildParams.create_code_params_script_builder(param_list[i], builder)
                builder.emit_push_integer(len(param_list[i]))
                builder.emit(PACK)
        return builder.to_array()

    @staticmethod
    def get_map_bytes(param_dict: {}):
        builder = ParamsBuilder()
        builder.emit(BuildParams.Type.maptype)
        builder.emit_push_integer(len(param_dict))
        return builder.to_array()
